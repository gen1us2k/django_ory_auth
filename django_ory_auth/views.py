from django.shortcuts import render

def logout(request):
    """
    View that clears cached auth data. Configure Ory to redirect here 
    on log out.
    """
    user_id_cache_key = f"userid_{request.COOKIES.get('sessionid')}"
    cache.delete(user_id_cache_key)
  
    logout_cache_key = f"logout_{request.COOKIES.get('sessionid')}"
    cache.delete(logout_cache_key)

    return redirect('logout_redirect_url_name')
