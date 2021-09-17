token = input("what is your bot token?\n->")
prefix = input("what do you want as prefix?\n->")
desc = input("do you like to add a small description? (5words long max)\n->")
code = '''const Discord = require("discord.js");
const client = new Discord.Client();

client.on("ready", () => {
  console.log(`Logged in as ${client.user.tag}!`);
  client.user.setActivity('DESC');
});

client.on("message", message => {
  if (message.content[0] == "PREFIX") {
  	var msg = message.content.replace('PREFIX', '');
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

client.login("TOKEN")
'''
code = code.replace('TOKEN', token)
code = code.replace('PREFIX', prefix)
code = code.replace('DESC', desc)
file = open("index.js", 'a')
file.write(''.join(code))
file.close()
