const express = require('express')
const app = express()
const bodyParser = require('body-parser');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));


app.get('/', (req, res) => res.send('Hello World!'))

app.post('/getdata',(req, res) => {
    var data = req.body;
    var title = data.title;
    var author = data.author;
    var content = data.content;
    var spawn = require("child_process").spawn;
    spawn('python',["./from_connection.py", title, author, content]);
    console.log(data);
    res.send("done");
})

app.post('/senddata',(req, res) => {
    var data = req.body;
    var title = data.title;
    var author = data.author;
    var content = data.content;
    // var spawn = require("child_process").spawn;
    // spawn('python',["./from_connection.py", title, author, content]);
    console.log(data);
    res.send("done");
})

app.listen(3000, () => console.log('Example app listening on port 3000!'))