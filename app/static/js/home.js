(function (win, doc){
    'use strict'

    if(doc.querySelector('.delete-btn')){
        let deleteBtn = doc. querySelectorAll('.delete-btn')
        for (let i = 0; i < deleteBtn.length; i++){
            deleteBtn[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este produto?')){
                    return true
                }else{
                    event.preventDefault()
                }
            })
        }
    }

})(window, document)