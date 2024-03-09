function MyFunction () {
    console.log("Thalapathy!");
    var fileURL = 'https://github.com/Saimohan2-4/Portfolio-sai/blob/main/DA__Saimohan%20S.pdf';
    
    // Create an anchor element
    var downloadLink = document.createElement('a');
    
    // Set the href attribute to the file URL
    downloadLink.href = fileURL;
    
    // Specify that the download attribute should be used
    downloadLink.setAttribute('download', 'https://github.com/Saimohan2-4/Portfolio-sai/blob/main/DA__Saimohan%20S.pdf');
    
    // Append the anchor element to the body
    document.body.appendChild(downloadLink);
    
    // Trigger the click event on the anchor element
    downloadLink.click();
    
    // Clean up: remove the anchor element from the body
    document.body.removeChild(downloadLink);
}
document.getElementById('downloadButton').addEventListener('click', function() {
    // Assuming your PDF file is named "example.pdf" and stored in the same directory
    var fileURL = 'https://github.com/Saimohan2-4/Portfolio-sai/blob/main/DA__Saimohan%20S.pdf';
    
    // Create an anchor element
    var downloadLink = document.createElement('a');
    
    // Set the href attribute to the file URL
    downloadLink.href = fileURL;
    
    // Specify that the download attribute should be used
    downloadLink.setAttribute('download', 'https://github.com/Saimohan2-4/Portfolio-sai/blob/main/DA__Saimohan%20S.pdf');
    
    // Append the anchor element to the body
    document.body.appendChild(downloadLink);
    
    // Trigger the click event on the anchor element
    downloadLink.click();
    
    // Clean up: remove the anchor element from the body
    document.body.removeChild(downloadLink);
});

function includeHTML() {
    var z, i, elmnt, file, xhttp;
    /*loop through a collection of all HTML elements:*/
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
      elmnt = z[i];
      /*search for elements with a certain attribute:*/
      file = elmnt.getAttribute("w3-include-html");
      if (file) {
        /*make an HTTP request using the attribute value as the file name:*/
        xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
          if (this.readyState == 4) {
            if (this.status == 200) {elmnt.innerHTML = this.responseText;}
            if (this.status == 404) {elmnt.innerHTML = "Page not found.";}
            /*remove the attribute, and call this function once more:*/
            elmnt.removeAttribute("w3-include-html");
            includeHTML();
          }
        }      
        xhttp.open("GET", file, true);
        xhttp.send();
        /*exit the function:*/
        return;
      }
    }
  };