const handleFiles = (files) => {
  const file = files[0];
  if (!file) return;

  const preview = document.getElementById("preview");
  const reader = new FileReader();
  reader.onload = function (e) {
    preview.src = e.target.result;
    preview.hidden = false;
  };
  reader.readAsDataURL(file);

  const formData = new FormData();
  formData.append("file", file);

  fetch("http://localhost:8000/predict", {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("class-name").innerText = data.class_name;
      document.getElementById("confidence").innerText = data.confidence;
      document.getElementById("result-box").hidden = false;
    })
    .catch((err) => {
      console.error("Prediction error:", err);
    });
};
