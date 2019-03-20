function authenticate(email, password){

    if(email==="admin@andela.ug" && password ==="andela256"){

        window.location.href = "./admin.html";
    }
    if (form.email.value == 'ivan@gmail.com' && form.pass.value == 'uganda'){
            
        window.location.href = "./user.html";
        } else{

           const errormessage = document.getElementById("error");
           errormessage.innerText = "Login Failed!"
       }

  }
  
  const loginForm = document.getElementById("form");
  
  loginForm.addEventListener("submit", (event)=>{
    event.preventDefault()
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value; 
    authenticate(email, password)

  })


 