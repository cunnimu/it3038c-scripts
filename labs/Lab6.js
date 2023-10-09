var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');
let uptime = os.uptime();
let days = Math.floor(uptime / 86400);
let hours = Math.floor(uptime / 3600) - (days * 24);
let minutes = Math.floor(uptime % 3600 / 60);
let seconds = Math.floor(uptime % 60);


http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${days} Hours: ${hours} Minutes: ${minutes} Seconds: ${seconds}</p>
            <p>Total Memory: ${os.totalmem() / 1000000} MB</p>
            <p>Free Memory: ${os.freemem() / 1000000} MB</p>
            <p>Number of CPUs: ${os.cpus().length}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000");
