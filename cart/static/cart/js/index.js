CEP_API_BASE_URL = 'https://viacep.com.br/ws'

$('#postal-code-input').keyup((e) => {
    this.code = $('#postal-code-input').val()
})

$('#search-code-btn').click((e) => {
    e.preventDefault()
    fetch_address(this.code)
    .then((result) => {
        set_address(result.logradouro)
    })
})

async function fetch_address(code) {
    const response = await fetch(`${CEP_API_BASE_URL}/${code}/json`, {
        method: 'GET',
        mode: 'cors',
        headers: {'Content-Type': 'application/json'}
    })
    const result = await response.json() 
    return result
}

function set_address(address) {
    $('#address-street-input').val(`${address}`)
}