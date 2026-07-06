function loadUsers() {

fetch("https://jsonplaceholder.typicode.com/users")

.then(response => response.json())

.then(users => {

let output = "";

users.forEach(user => {

output += `

<div class="card">

<h3>${user.name}</h3>

<p>Email : ${user.email}</p>

<p>City : ${user.address.city}</p>

<p>Company : ${user.company.name}</p>

</div>

`;

});

document.getElementById("users").innerHTML = output;

})

.catch(error => {

console.log(error);

});

}