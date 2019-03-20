function email(evt, emailTab) {
    // Declare all variables
    var i, tabcontent, tablinks;
  
    // Get all elements with class="tabcontent" and hide them
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Get all elements with class="tablinks" and remove the class "active"
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
  
    // Show the current tab, and add an "active" class to the link that opened the tab
    document.getElementById(emailTab).style.display = "block";
    evt.currentTarget.className += " active";
  }
  $(function() {
    $( ".tablinks" ).tabs({
      activate:function(event,ui){

        localStorage.setItem("lastTab",ui.newTab.index() );
      },
      active: localStorage.getItem("lastTab") || 0
    });
 });
  

  function required()
  {
  var empt = document.form.textarea.value;
  if (empt === "")
  {
  alert("Message empty..");
  return false;
  }
  else 
  {
  alert('Message Sent!');
  return true; 
  }
  }

  