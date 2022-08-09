CEP_API_BASE_URL = 'https://viacep.com.br/ws'

$('.form-control').keyup((e) => {
    this.code = $('.form-control').val()
})

$('#check-code-btn').click((e) => {
    e.preventDefault()
    fetch_address(this.code)
    .then((result) => {
        set_address(result.logradouro)
    })
})

async function fetch_address(code) {
    const response = await fetch(`${CEP_API_BASE_URL}/${code}/json`)
    const result = await response.json() 
    return result
}

function set_address(address) {
    $('#address').text(`${address}`)
}