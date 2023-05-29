function getExtension(filename) {
  var parts = filename.split('.');
  return parts[parts.length - 1];
}

function isImage(filename) {
  var ext = getExtension(filename);
  switch (ext.toLowerCase()) {
    case 'jpg':
    case 'gif':
    case 'bmp':
    case 'png':
      return true;
  }
  return false;
}

function bottles_found() {
    Swal.fire({
        title: 'Теперь потвердите вашу находку/(-ки)!',
        html:
            '<input type="file" class="form-control-file image-input"></br></br>',
        showConfirmButton: true,
        confirmButtonText: 'Потвердить'
    }).then((_) => {
        var image = $(".image-input");

        if (!isImage(image.val()))
        {
            Swal.fire({
                icon: 'error',
                title: 'Упс..',
                text: 'Кажется, что файл который вы прикрепили не является изображением',
            });
            return;
        }

        var formData = new FormData();
        formData.append('image', $('.image-input')[0].files[0]);
        $.ajax({
            url: '/api/bottles_found/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                Swal.fire({
                    icon: 'success',
                    title: 'Спасибо!',
                    text: 'Мы увеличим количество бутылок в вашем аккаунте в скором времени!'
                })
            }
        })
    })
}
