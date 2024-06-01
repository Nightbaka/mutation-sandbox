import { UserManager } from 'oidc-client';

const userManager = new UserManager({
  authority: 'https://accounts.google.com',
  client_id: '39509314769-c2f05oefah75st584d3f9cuibqsamu2h.apps.googleusercontent.com',
  redirect_uri: 'http://localhost:8000/accounts/google/login/callback/',
  response_type: 'code',
  scope: 'openid email profile',
  post_logout_redirect_uri: 'http://localhost:8000/',
});

export default userManager;
