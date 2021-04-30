function returndata(data_set){
    for(let i=0;i<5;i++){
    
    let recipe_name=data_set.recipes[i].title
    let recipe_image=data_set.recipes[i].image_url
    let author_name=data_set.recipes[i].publisher
    html_content=" "
    html_content+=`<div class="card" style="width: 18rem;">
    <img src="${recipe_image}" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">Recipe:${recipe_name}</h5>
      <p>Author:${author_name}</p>
    </div>`
    document.querySelector("#resltarea").innerHTML+=html_content
}
}




function getdata(){
    let recipe_name=document.querySelector("#recipy").value 
    let url=`https://forkify-api.herokuapp.com/api/search?q=${recipe_name}`
    fetch(url).
    then(responce=>{
        if(!responce.ok){
            throw new Error("failed to fetch data");
        }
        else{
            return responce.json()
            // .then(data=>console.log(data));
        }
        
    })
    .then(data=>returndata(data))
    .catch(err=>alert(err.message))
}

