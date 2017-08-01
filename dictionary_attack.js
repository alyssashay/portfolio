var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true; 
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init;


/* ADD YOUR CODE BELOW */

function checkPassword() {
	console.log(wordsList);
	var password = document.getElementById("pw").value.toLowerCase();
	console.log(password);
	for (var x = 0; x< wordsList.length; x++)
	{
		if (password == wordsList[x]) {
					x = wordsList.length;
					document.getElementById("results").innerHTML = "Password is not valid. Please choose another password.";

		}else{
			document.getElementById("results").innerHTML = "Password is strong!!";
		}

		if(password.length < 6) {
					x = wordsList.length;
					document.getElementById("results").innerHTML = "Password is too short. Please choose another password.";
		}else{
			document.getElementById("results").innerHTML = "Password is at good length!";
		}
		
		
	}

}