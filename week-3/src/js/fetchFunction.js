// import fetch from "cross-fetch";

async function fun(num) {
  const reponse = await fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
  );
  let data = await reponse.json();
  if (flag === 0) {
    areaTopElementAdd(data);
    flag = 1;
  }

  areaCenterElementAdd(data, num);
}
function areaTopElementAdd(data) {
  let el = document.getElementById("areaTop");

  for (let i = 0; i < 2; i++) {
    let title = data["result"]["results"][i]["stitle"];
    let str = data["result"]["results"][i]["file"].split(":")[1].slice(0, -5);

    let newDiv = document.createElement("div");
    newDiv.className = "grid-promotion-item ";

    let newImg = document.createElement("img");
    newImg.src = "https:" + str;
    newImg.width = 75;
    newImg.height = 50;

    let newA = document.createElement("a");
    let newContent = document.createTextNode(title);

    newA.appendChild(newContent);
    newDiv.appendChild(newImg);
    newDiv.appendChild(newA);
    el.appendChild(newDiv);
  }
}

function areaCenterElementAdd(data, n) {
  let el = document.getElementById("areaCenter");
  let num = 2 + n;
  for (let i = num - 8; i < num; i++) {
    if (i < data["result"]["results"].length) {
      let title = data["result"]["results"][i]["stitle"];
      let str = data["result"]["results"][i]["file"].split(":")[1].slice(0, -5);

      let newDiv = document.createElement("div");
      newDiv.className = "grid-tittle-item";

      let newBox = document.createElement("div");
      newBox.className = "imgBox";

      let newImg = document.createElement("img");
      newImg.src = "https:" + str;
      newImg.width = 220;
      newImg.height = 150;

      let newIcon = document.createElement("i");
      newIcon.className = "icon fas fa-star";

      let newA = document.createElement("a");
      let newContent = document.createTextNode(title);

      newA.appendChild(newContent);
      newDiv.appendChild(newImg);
      newDiv.appendChild(newIcon);
      //newBox.appendChild(newA);
      newDiv.appendChild(newA);
      el.appendChild(newDiv);
    }
    else{
      console.log(data["result"]["results"].length)
      document.getElementById("loadMore").style.display = 'none';
      alert("已顯示全部");
      break;
    }
  }
}
let num = 8;
let flag = 0;
fun(num);

function loadmore() {
  num = num + 8;
  fun(num);
}
