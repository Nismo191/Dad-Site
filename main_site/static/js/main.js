function processModal(data){
    // Get the modal
    var modal = document.getElementById("modal");

    for(var i = 0; i < photo_data.length; i++){
      if(data.id == photo_data[i].pk){
        var url = photo_data[i].fields.image
      }
    }

    // Get the image and insert it inside the modal - use its "alt" text as a caption
    var img = document.getElementById(data.id);
    var modalImg = document.getElementById("img-m");
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    modalImg.src = "/media/"+url
    captionText.innerHTML = img.alt;

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }
}


function zoom() {
  var element = document.getElementById("img-m");
  element.classList.toggle("zoom");
}


window.onload = function(){
    var coll = document.getElementsByClassName("collapsible");
    var i;

    for (i = 0; i < coll.length; i++) {
        coll[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight){
                content.style.maxHeight = null;
              } else {
                content.style.maxHeight = content.scrollHeight + "px";
              }
            });
    }
}


