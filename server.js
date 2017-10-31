const express = require('express')
const _ = require('lodash');
const app = express();

const userTemplate = {
	blocked: false,
	runningRequests: 0,
};

let database = {};
setInterval(() => {
	console.log('reseting database');
	database = {};
}, 1000 * 60 * 60 * 24); // clear database every 24 hours

function unblockApp(appKey) {
	console.log(`unblocking app - ${appKey}`);
	const appRecord = database[appKey];
	if (_.isNil(appRecord)) return;
	appRecord.blocked = false;
}

const REQUESTS_LIMITATION = 5;
const BLOCK_TIME = 3 * 1000; // Three seconds
function rateLimiting(appKey) {
	appRecord = database[appKey];
	if (_.isNil(appRecord)) {
		console.log(`new app - ${appKey}`);
		appRecord = _.assign({}, userTemplate);
		database[appKey] = appRecord;
	}

	if (appRecord.blocked) {
		console.log(`application ${appKey} request has been denied - app blocked`);
		return false;
	}
	if (appRecord.runningRequests >= REQUESTS_LIMITATION) {
		console.log(`application ${appKey} has broke the rate limit - blocking app`);
		appRecord.blocked = true;
		setTimeout(unblockApp, BLOCK_TIME, appKey);
		return false;
	}

	appRecord.runningRequests += 1;
	console.log(`application ${appKey} current runningRequests: ${appRecord.runningRequests}`);
	return true;
}

function rollTheDice() {
	return Math.floor(Math.random() * 6) + 1; // Between 1 - 6
}

function sendResponse(res, appKey) {
	res.setHeader('Content-Type', 'application/json');
	const result = rollTheDice();
	res.send(JSON.stringify({ result }));
	database[appKey].runningRequests -= 1;
	console.log(`application ${appKey} rolled ${result}`);
}

const DICE_DELLY = 900; // miliseconds
app.get('/', function (req, res) {
	if (_.isNil(req.query.app) || _.isNil(req.query.throw)) {
		res.status(400).send('Requet must contain an app key and a throw id');
		return;
	}

	if (!rateLimiting(req.query.app)) {
		res.status(400).send('RATE LIMIT REACHED!');
		return;
	}

	setTimeout(sendResponse, DICE_DELLY, res, req.query.app);
})

app.listen(8875, function () {
	console.log('Example app listening on port 8875!')
})