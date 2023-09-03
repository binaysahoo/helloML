const redis  = require('redis');

const client = redis.createClient({
  host: 'localhost', // Redis server hostname
  port: 6379        // Redis server port
});

(async () => {
    await client.connect();
})();

client.on('ready', () => {
    console.log("Connected!");
});  
client.on('error', (err) => {
    console.error(err);
});

(async () => {    
    await client.set('username', 'binayk');
})();

(async () => {    
   const value = await client.get("username");
   console.log("value:"+value);     
})();

(async () => {    
    await client.hSet('empdetails', {
        name: 'binay',
        surname: 'sahoo',
        company: 'snps',
        joined: 2010
    });
})();   


(async () => {    
    let userSession = await client.hGetAll('empdetails');
    console.log(JSON.stringify(userSession, null, 2));
})();   

/*

 */
