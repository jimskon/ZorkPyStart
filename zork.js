// you will need to generate a unique id for each user
var id="jimskon"

var world;

// Add a click event for the command button
document.querySelector("#command-btn").addEventListener("click", (e) => {
    command();
});

var input = document.getElementById("command");
// Respond to enter key
input.addEventListener("keyup", function(event) {
    // Number 13 is the "Enter" key on the keyboard
    if (event.keyCode === 13) {
        // Cancel the default action, if needed
        event.preventDefault();
        // Trigger the button element with a click
        command();
    }
});

processCommand("Start");


// Print to terminal, and clear the input
function printLine(text) {
    term = document.getElementById("term")
    term.innerHTML = term.innerHTML+text+"<br />";
    term.scrollTop = term.scrollHeight;
}

//Input and process Command
// Called from submit button or enter
function command() {
  com=document.getElementById("command").value;
  printLine("<span style='color:blue'>>>> "+com+"</span>");
  processCommand(com.toLowerCase());
}

function processCommand(command) {
    if (command.length<1) {
      return;
    }
    command = command.split(' ').join('+');
    console.log(command,id);
    fetch('/cgi-bin/skon_gamewebclient.py?id=' + id + '&command=' + command, {
	method: 'get'
    })
	.then (response => response.text() )
        .then (data => processResults(data))
	.catch(error => {
	    {alert("Error: Something went wrong:"+error);}
	})
}


function processResults(results) {
  console.log(results);
  printLine(results);
}
