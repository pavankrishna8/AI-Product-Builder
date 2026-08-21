\## Input

"Build a feature that lets users reset their password via email, with a 15-minute

expiring link, for our existing web app."



\## Output (verified, Day 3)

{

&#x20; "status": "ready",

&#x20; "problem": "Users who forget their passwords cannot access their accounts and need a secure, self-service method to regain access without contacting support.",

&#x20; "target\_users": "Registered users who have forgotten their passwords.",

&#x20; "goals": \[

&#x20;   "Enable users to securely reset their passwords without administrative intervention.",

&#x20;   "Minimize security risks associated with password recovery by enforcing a short link expiration window.",

&#x20;   "Reduce support overhead for password-related inquiries."

&#x20; ],

&#x20; "requirements": \[

&#x20;   "Provide a 'Forgot Password' link on the login page.",

&#x20;   "Allow users to input their registered email address to request a password reset.",

&#x20;   "Send an email containing a unique, secure, and single-use password reset link.",

&#x20;   "Enforce a strict 15-minute expiration time limit on the password reset link.",

&#x20;   "Render an error page for expired or invalid links.",

&#x20;   "Provide a form for the user to input and confirm a new password upon clicking a valid link.",

&#x20;   "Enforce existing password strength policies on the new password input.",

&#x20;   "Update the user's password and invalidate the reset token immediately upon successful submission."

&#x20; ],

&#x20; "open\_questions": \[

&#x20;   "Should we implement a generic success message to prevent user enumeration?",

&#x20;   "Should we implement rate limiting on password reset requests?",

&#x20;   "Should resetting the password invalidate all other active sessions for that user?"

&#x20; ]

}

