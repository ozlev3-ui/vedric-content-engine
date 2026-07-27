# Deployment

## Temporary staging

The app currently lives under `mybh-app/` on a dedicated branch. In Vercel, set the Root Directory to `mybh-app`.

## Environment variables

- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY`

## Final repository

The intended production repository is `ozlev3-ui/mybh-flow`. Once created, copy the contents of `mybh-app/` to its root and connect that repository to Vercel.

## Do not deploy

Do not deploy the repository root as MYBH. The root belongs to Vedric Content Engine.
