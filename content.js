// const extensionAPI = typeof browser === 'undefined' ? chrome : browser;

checked = []
let currentDomain = document.domain;
function scantexts() {


  console.log(currentDomain)


  let elements = segments(document.body);
  for (let i = 0; i < elements.length; i++) {
    if (!(elements[i] && elements[i].innerText)) {
      continue;
    }
    if (checked.includes(elements[i])) {
      continue;
    }
    console.log(elements[i].innerText);
    const postData = { q: elements[i].innerText, source: "en", target: "hi", format: "text", api_key: "" }
    makecall(postData, elements[i])
    checked.push(elements[i])

  }
}

async function makecall(postdata, ele) {
  const response = await fetch('http://127.0.0.1:5000/translate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    mode: 'cors',
    body: JSON.stringify(postdata),
  });

  const responseText = await response.text();
  console.log('Server response:', responseText);
  try {
    ele.setAttribute('originial-text', postdata.q.toString())
    const data = JSON.parse(responseText);
    console.log('Parsed JSON:', data);
    var newtext = data.translatedText.toString();
    ele.innerText = newtext;
  } catch (error) {
    console.error('JSON parsing error:', error);
  }
}


function sendImageToApi(imageUrl) {
  const apiUrl = "http://127.0.0.1:8000/translate/image/";

  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ imgurl: imageUrl, language: 'hi' }),
  })
    .then(response => response.json())
    .then(data => {
      console.log("API Response:", data);

      const imageElement = document.querySelector(`img[src="${imageUrl}"]`);
      if (imageElement) {
        const textElement = document.createElement("div");
        textElement.textContent = data.translated.toString();

        textElement.style.border = "2px solid red";
        console.log("*****************8", data.translated.toString())

        imageElement.parentNode.insertBefore(textElement, imageElement);
      }
    })
    .catch(error => {
      console.error("Error sending image to API:", error);
    });
}

function scanfiles() {
  allatag = document.querySelectorAll('a');
  allatag.forEach(function (link) {
    if (link.href.includes('.pptx')) {
      pptDownloadUrl = link.href;

      const form = new FormData();
      const fileUrl = pptDownloadUrl; // Replace with your actual file URL
      
      // Function to download the file
      const downloadFile = async (url) => {
        const response = await fetch(url);
        const blob = await response.blob();
        form.append("file", blob, "file.pptx"); // Append the blob to the FormData
      };
      
      // Download the file and append it to the FormData
      downloadFile(fileUrl)
        .then(() => {
          form.append("source", "en");
          form.append("target", "hi");
          form.append("api_key", "");
      
          const options = {
            method: 'POST',
            headers: {
              cookie: 'session=093a26b6-1abf-4aa2-abad-4fbc04f41066',
            },
            body: form
          };
      
          fetch('http://127.0.0.1:5000/translate_file', options)
            .then(response => response.json())
            .then(response => console.log(response))
            .catch(err => console.error(err));
        });
      
    }
  });
}

window.addEventListener('load', function () {
  // const images = document.querySelectorAll("img");
  // const imageUrls = Array.from(images).map(img => img.src);

  // imageUrls.forEach((imageUrl, index) => {
  //   setTimeout(() => {
  //     sendImageToApi(imageUrl);
  //   }, index * 2000);
  // });
  // scantexts();
  scanfiles();
});

extensionAPI.runtime.onMessage.addListener(function (request, sender, sendResponse) {
  if (request.action === "reportText") {

    reportText(request.selectedText);
  }
  if (request.action === "wrongText") {
    revert()
    alert("Re translated again")
  }
  if (request.action === "playText") {
    const apiUrl = "http://127.0.0.1:8000/translate/audio/";

    fetch(apiUrl, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: request.selectedText }),
    })
      .then(response => response.json())
      .then(data => {
        var soundFileName = data.path;
        var soundFile = soundFileName.replace('//', '/')
        console.log(soundFile)
      })
      .catch(error => console.error('API error:', error));
  }
});

function revert() {
  const textElements = document.querySelectorAll('[originial-text]');
  textElements.forEach(function (element) {
    let value = element.getAttribute('originial-text');
    console.log(value)
    console.log(element)
    element.innerText = value;
  });
}

function reportText(selectedText) {
  const apiUrl = "http://127.0.0.1:8000/translate/summarize/";

  fetch(apiUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ artical: selectedText }),
  })
    .then(response => response.json())
    .then(data => {
      console.log("API Response:", data);
      alert(data.summary.toString())
    })
}

// function handleChanges() {
//   scantexts();
// }
// const observer = new MutationObserver(handleChanges);

// const config = { childList: true, subtree: true };

// observer.observe(document.body, config);

// handleChanges();