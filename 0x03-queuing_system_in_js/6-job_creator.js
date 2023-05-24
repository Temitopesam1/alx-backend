import { createQueue } from 'kue';

const queue = createQueue();

const job = queue.create('push_notification_code', {
	phoneNumber: '4153518780',
  	message: 'This is the code to verify your account'
});
job.on('complete', (result) =>{console.log('Notification job completed')});
job.on('failed attempt', (errorMessage, doneAttempts) =>{
	console.log('Notification job failed');
});
job.save((err) =>{
	if(!err)
		console.log(`Notification job created: ${job.id}`);
});
