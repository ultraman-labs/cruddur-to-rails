-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Tony Quintanilla', 'nodaltech@outlook.com', 'Ultra-Man' ,'50790df1-cc21-4ea3-8f43-a064d4cf07b2'),
  ('Cassidy Tuck', 'techfixer@live.com', 'Ultra-Girl' ,'53b535ba-864b-447b-a1bc-026a4ddd1f0e');
  ('Londo Mollari', 'lmollari@centari.com', 'londo' ,'MOCK');


INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'Ultra-Man' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
