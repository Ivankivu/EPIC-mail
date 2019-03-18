
//login form


function authenticate(email, password){

    if(email==="admin@andela.ug" && password ==="andela256"){
        console.log("success")
        //redirect to admin
        window.location.href = "./admin.html";
    }
    if (form.email.value == 'ivan@gmail.com' && form.pass.value == 'uganda'){
            //redirect to user
        window.location.href = "./user.html";
        }

       else{
           console.log("login failed ");
       }

  // am browsing  the file to find out how the check function is being called
      // if (form.email.value == "admin@andela.ug" && form.pass.value == "andela256"){
      //     window.open('admin.html')
      // }
      // if (form.email.value == 'ivan@gmail.com' && form.pass.value == 'uganda'){
      //     window.open('user.html')
      // }
      // else{
      //     alert("Error Password or Username");
      //     window.location.href('index.html');
      // }
  }
  
  const loginForm = document.getElementById("form");
  
  loginForm.addEventListener("submit", (event)=>{
    event.preventDefault()
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value; 
    console.log("form submitted")
    console.log("pass ",password)
    console.log("email ", email)
    authenticate(email, password)

  })
  
 