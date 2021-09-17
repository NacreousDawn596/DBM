const Discord = require("discord.js");
const client = new Discord.Client();

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
  client.user.setActivity('still dont know what I am doing ;-;');
});

client.on("message", message => {
  if (message.content[0] == "?") {
  	var msg = message.content.replace('?', '');
  	switch (msg.split(" ")[0].toLowerCase()) {
  		case "hello":
  			message.channel.send("hi")
  			break;
  		case "ping":
  			message.channel.send("pong")
  			break;
  	}
  }
});

client.login("ODIzOTgxMjQ0NDk2MzQ3MTY3.YFouVQ.qfpvUJyzN82pjf1MS42Jzg3qYsk")
