function email(evt, emailTab) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
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

  document.querySelector("#formAd").addEventListener("submit", function(e){
    if(!isValid){
        e.preventDefault();
        alert("Group added!");
        return false;
    }else{
      alert("failed!!")
    }
});
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}
