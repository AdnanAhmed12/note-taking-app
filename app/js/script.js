if (typeof jQuery === 'undefined') {
    console.error('jQuery is not loaded.');
} else {
    $(document).ready(function () {
        $("#addNoteForm").on("click", ".btn-primary", function (){
            // event.preventDefault();
            var noteTitle = $("input[name='note_title']").val();
            var noteText = $("#note_text").val();
            var noteColor = $("select[name='note_color']").val();
            // console.log(noteText)
            if (noteText.trim() === "") {
                alert("Note text cannot be empty!");
                return;
            }
            $.ajax({
                type: "POST",
                url: "/add_note",
                data: {
                    note_title: noteTitle,
                    note_text: noteText,
                    note_color: noteColor
                },
                success: function (response) {
                    if (typeof response === "string") {
                        var newNoteHtml = '<div class="col-md-4 note ' + noteColor + '" data-note-id="' + response.id + '">' +
                                  '<p>' + noteTitle + '</p>' +
                                  '<p>' + noteText + '</p>' +
                                  '<button class="btn btn-danger deleteNoteBtn">Delete</button>' +
                                  '</div>' ;
                        $("#noteContainer").prepend(newNoteHtml);
                        // $("#noteContainer").append(response);
                    } else if (typeof response === "object") {
                        var newNoteHtml = '<div class="col-md-4 note ' + response.color + '" data-note-id="' + response.id + '">' +
                                  '<p>' + response.title + '</p>' +
                                  '<p>' + response.description + '</p>' +
                                  '<button class="btn btn-danger deleteNoteBtn">Delete</button>' +
                                  '</div>';
                        $("#noteContainer").prepend(newNoteHtml);
                                }

                    
                    $("#addNoteForm")[0].reset();
                },
                error: function (error) {
                    console.error("Error adding note:", error);
                }
            });
        });

        $("#noteContainer").on("click", ".deleteNoteBtn", function () {
            var $deleteBtn = $(this);  
            var noteId = $deleteBtn.closest(".note").data("note-id");
              // console.log(noteId)
            $.ajax({
                type: "POST",
                note_id: noteId,
                url: "/delete_note/" + noteId,
                success: function () {
                    $deleteBtn.closest(".note").remove();
                    console.log(noteId) 
                },
                error: function (error) {
                    console.error("Error deleting note:", error);
                }
            });
        });

        $("#noteContainer").on("click", ".editNoteBtn", function () {
            var editBtn = $(this);
            var noteId = editBtn.closest(".note").data("note-id");

            var titleElement = $(this).siblings(".note-title");
            var contentElement = $(this).siblings(".note-content");
        
            var newTitle = prompt("Enter new title:", titleElement.text());
            var newContent = prompt("Enter new content:", contentElement.text());

        $.ajax({
            type: "POST",
            url: "/edit_note/" + noteId,
            data: {
                new_title: newTitle,
                new_content: newContent
            },
            success: function (response) {
                titleElement.text(response.title);
                contentElement.text(response.description);
            },
            error: function (error) {
                console.error("Error editing note:", error);
            }
            });
        })
    });
}