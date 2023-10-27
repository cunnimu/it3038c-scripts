var http = require("http");
var fs = require("fs");

http.createServer(function(req, res){
	if (req.url === "/log") {
		fs.readFile("/var/log/secure", "UTF-8", function(err, info){
	
	html = `
	<!DOCTYPE html>
	<html>
	<head>
	<title>Secure Log</title>
	</head>
	<body>
	<h1>Secure Log</h1>
	${info.replace(/\n/g, '<br>')}
	</body>
	</html>
`
	res.writeHead(200, {"Content-Type": "text/html"});
	res.write(html);
	res.end();
});
}
	else {
		res.writeHead(404, {"Content-Type": "text/plain"});
		res.end(`404 File Not Found at ${req.url}`);
}


}).listen(3000);

console.log("Server listening on port 3000");
