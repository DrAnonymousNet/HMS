let dept = document.getElementById("departmentlist")
console.log(dept)
let text = dept.options[dept.selectedIndex].text
console.log(text)
e = dept.addEventListener("change", getDoctor(text))

function get_doctors(text){
         console.log(text)
        let xhr = new XMLHttpRequest
        xhr.open("GET", "{% url 'appointment'%}", true)
        xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest")
        xhr.setRequestHeader("Context"
        let data = JSON.stringify({dept:text})

        xhr.onload = function(){
            let docs = JSON.parse(xhr.responseText)
            let opt = document.getElementById("doctor_opt")
            for (let doc of docs){
                opt.ParentElement.AppendChild(`<option> ${doc} </option>`)
                }
             }
        xhr.send(data)
        }
