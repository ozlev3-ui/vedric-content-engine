# MYBH Flow

Clean Next.js staging app for the MYBH health platform.

This directory is intentionally isolated from Vedric. It exists only as a temporary migration workspace until the code is moved into a dedicated `mybh-flow` repository.

## Stack

- Next.js 16.2.11
- React 19
- TypeScript
- Tailwind CSS
- Supabase-ready environment variables

## Current scope

- Dashboard
- Water tracking
- Meals tracking
- Movement tracking
- Sleep tracking
- Weight and wellbeing logging
- Local persistence through localStorage

## Next infrastructure steps

1. Move this directory into a dedicated repository.
2. Create a Supabase project.
3. Add Auth, PostgreSQL tables, Storage and Row Level Security.
4. Replace localStorage with authenticated database persistence.
5. Deploy to Vercel.
