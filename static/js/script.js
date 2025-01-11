// document.addEventListener("DOMContentLoaded", function() {
//   const menuIcon = document.querySelector(".menu_icon");
//   const navbarOption = document.querySelector(".navbar_option");
//
//   let state = 0;
//
//   menuIcon.addEventListener("click", function() {
//     if (state === 0) {
//       navbarOption.style.display = "block";
//       navbarOption.style.left = "0px";
//       navbarOption.classList.add("show");
//       state = 1;
//     } else {
//       navbarOption.classList.remove("show");
//       navbarOption.style.left = "-100%";
//       setTimeout(() => {
//         navbarOption.style.display = "none";
//       }, 300); // Delay the display:none; change to match the animation duration
//       state = 0;
//     }
//   });
// });


// document.addEventListener("DOMContentLoaded", function() {
//   const videoElement = document.getElementById("videoStream");
//
//   // Check if the browser supports getUserMedia
//   if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//     // Access the user's camera
//     navigator.mediaDevices.getUserMedia({ video: true })
//       .then(function(stream) {
//         // Display the camera stream in the video element
//         videoElement.srcObject = stream;
//       })
//       .catch(function(error) {
//         console.error("Error accessing the camera: ", error);
//       });
//   } else {
//     console.error("getUserMedia is not supported in this browser.");
//   }
// });




// Signal

// Get a reference to the "Signal" menu option element
const signalMenuSignal = document.querySelector('.menu_option.Signal');
// Get a reference to the div where the dynamic content will be loaded
const dynamicContentSignal = document.getElementById('dynamic-content');
// Add a click event listener to the "Signal" menu option
signalMenuSignal.addEventListener('click', () => {
  // Use Ajax to load the Points.html content from the /points route
  fetch('/points')
    .then(response => response.text())
    .then(htmlContent => {
      // Replace the content of the dynamicContentDiv with the loaded Points.html content
      dynamicContentSignal.innerHTML = htmlContent;
    })
    .catch(error => {
      console.error('Error loading Points.html:', error);
    });
});

// Signal

// Get a reference to the "Signal" menu option element
const signalMenuData = document.querySelector('.menu_option.data');
// Get a reference to the div where the dynamic content will be loaded
const dynamicContentData = document.getElementById('dynamic-content');
// Add a click event listener to the "Signal" menu option
signalMenuData.addEventListener('click', () => {
  // Use Ajax to load the Points.html content from the /points route
  fetch('/dataset')
    .then(response => response.text())
    .then(htmlContent => {
      // Replace the content of the dynamicContentDiv with the loaded Points.html content
      dynamicContentData.innerHTML = htmlContent;
    })
    .catch(error => {
      console.error('Error loading Points.html:', error);
    });
});


// Get a reference to the "Signal" menu option element
const signalMenuResearch = document.querySelector('.menu_option.research');
// Get a reference to the div where the dynamic content will be loaded
const dynamicContentResearch = document.getElementById('dynamic-content');
// Add a click event listener to the "Signal" menu option
signalMenuResearch.addEventListener('click', () => {
  // Use Ajax to load the Points.html content from the /points route
  fetch('/research-paper')
    .then(response => response.text())
    .then(htmlContent => {
      // Replace the content of the dynamicContentDiv with the loaded Points.html content
      dynamicContentResearch.innerHTML = htmlContent;
    })
    .catch(error => {
      console.error('Error loading Points.html:', error);
    });
});





document.addEventListener("DOMContentLoaded", function() {
  // Store the URL of the home page
  const homePageURL = '/home';

  // Use event delegation to handle clicks on dynamic content
  document.addEventListener('click', (event) => {
    const target = event.target;

    // Check if the clicked element is the "video" button
    if (target.id === "video") {
      // Prevent the default behavior (page reload)
      event.preventDefault();

      // Use JavaScript to navigate to the home page
      window.location.href = homePageURL;
    }

    // Add other click event handling logic here
    // For example, check if the element is a "Signal" menu option
    if (target.classList.contains('menu_option')) {
      // Use AJAX to load content
      // ...
    }
  });

  // Other JavaScript code for your application
  // ...
});

