function req(){
    var name = document.comment_post.Name.value;
    var email = document.comment_post.Email.value;
    var feed = document.comment_post.feed.value;

    if (name == null || name == ''){
        alert('Name cannot be empty!!!!!!................')
        return false
    }

    if (email == null || email == ""){
        alert('Email cannot be empty!!!!!!................')
        return false
    }

    if (feed == null || feed == ""){
        alert(' please feel free to write your comments....... ')
        return false
    }

}