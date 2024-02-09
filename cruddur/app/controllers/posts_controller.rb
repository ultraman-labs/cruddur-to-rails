class PostsController < ApplicationController
    def index
      @posts = Post.all
    end
  
    # other actions (show, new, edit, etc.) go here
  end
  