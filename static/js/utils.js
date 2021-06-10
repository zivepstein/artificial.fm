var next_song = function(x){
      console.log("next song is....")
      console.log(x)
      var current_id = songList[parseInt(x)]['song_id'];
      $("#modality").attr("song_id" , current_id);
      var local_questions = JSON.parse(JSON.stringify(questions))
      local_questions = local_questions.sort(() => Math.random() - 0.5)

      $("#modality").text(local_questions[0]);
      $(".subjectiveOuter").removeClass('magictime boingOutDown');
      $(".subjectiveOuter").addClass('magictime boingInUp');
      state['question_number'] = 0;
    }