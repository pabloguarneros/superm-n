import{Magic}from'magic-sdk';import{OAuthExtension}from'@magic-ext/oauth';const magic=new Magic('YOUR_API_KEY',{extensions:[new OAuthExtension()],});await magic.oauth.loginWithRedirect({provider:'...',redirectURI:'https://your-app.com/your/oauth/callback',scope:['user:email'],});const result=await magic.oauth.getRedirectResult();interface OAuthRedirectResult{oauth:{provider:string;scope:string[];accessToken:string;userHandle:string;userInfo:...;};magic:{idToken:string;userMetadata:MagicUserMetadata;};};