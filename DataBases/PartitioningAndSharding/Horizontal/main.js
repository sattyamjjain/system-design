const MongoClient = require('mongodb').MongoClient;
const uri = "mongodb+srv://<username>:<password>@<cluster>.mongodb.net/test?retryWrites=true&w=majority";
const client = new MongoClient(uri, { useNewUrlParser: true });
client.connect(err => {
  if (err) throw err;
  const database = client.db("mydatabase");
  database.createCollection("mycollection", {
    shardKey: { name: 1 }
  }, function(err, res) {
    if (err) throw err;
    console.log("Collection created!");
    client.close();
  });
});