import { createClient, print } from 'redis';
import { promisify } from 'util';
const client = createClient();


function setNewSchool(schoolName, value){
	client.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName){
	const result = await promisify(client.get).bind(client)(schoolName);
	console.log(result);
}

async function main(){
	await displaySchoolValue('Holberton');
	setNewSchool('HolbertonSanFrancisco', '100');
	await displaySchoolValue('HolbertonSanFrancisco');
}

client.on('connect', async () => {
	console.log("Redis client connected to the server");
	await main();
})
client.on('error', err => console.log('Redis client not connected to the server: ', err.toString()));
