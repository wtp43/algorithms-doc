# CORS and CSRF

  
It's not a security mechanism in the sense of preventing you from accessing information. It's a security mechanism to prevent attacks like CSRF.

Without CORS, any site could send a request to your banking site requesting to transfer all your money. If you were logged in, the request would be sent with cookies and authenticated. CORS prevents that request from being sent.

## You can't bypass CORS policy using a proxy

**tl;dr**: The proxy can make a request on your behalf, but nothing malicious will happen. This is because browsers don't send cookies from one domain to another domain.

---
**Longer example**:

Suppose, you're logged into **bank.com** on one tab, and open **evil.com** in another tab.

If there were no CORS mechanism, **evil.com** can make AJAX request to **bank.com** (this is known as a cross-origin request) without your knowledge. And along with the request, the browser will send the session cookie which was set by **bank.com** earlier when you logged in. With this session cookie, **bank.com** will think that you've made this request and will process it.

With the CORS mechanism, the browser will first check whether **bank.com** accepts cross-origin requests or not. For this, the browser will first send an OPTIONS request to **bank.com**. The browser will only send the actual request if **bank.com**'s CORS policy allows it.

Now, suppose **evil.com** tries to "bypass" this using a proxy. It will make an AJAX request to **proxy.com** which will forward the request to **bank.com**.

But now, the browser will only send the cookies set by **proxy.com**. So, the **bank.com**'s server will not get your session cookie and the attack will not work.

As you can see, using a proxy doesn't help in this case.

