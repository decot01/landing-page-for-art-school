function disableButton() {
    var button = document.getElementById("myButton");
    button.disabled = true;
    button.innerHTML = "Ваша заявка принята";
  }

  async function AddToDB() {
    const input = document.getElementById('inputText').value;
    console.log(input);

  }
  
