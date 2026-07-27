create table if not exists public.profiles (
  id uuid primary key references auth.users(id) on delete cascade,
  display_name text,
  birth_date date,
  height_cm numeric,
  current_weight_kg numeric,
  water_goal_ml integer default 2500,
  goals text[] default '{}',
  medical_conditions text,
  created_at timestamptz default now(),
  updated_at timestamptz default now()
);

create table if not exists public.daily_logs (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  log_date date not null default current_date,
  water_ml integer default 0,
  movement_minutes integer default 0,
  sleep_hours numeric,
  feeling text,
  unique(user_id, log_date)
);

create table if not exists public.meal_logs (
  id bigint generated always as identity primary key,
  user_id uuid not null references auth.users(id) on delete cascade,
  eaten_at timestamptz default now(),
  meal_type text,
  description text,
  calories integer,
  protein_g numeric,
  carbs_g numeric,
  fat_g numeric,
  image_path text
);

alter table public.profiles enable row level security;
alter table public.daily_logs enable row level security;
alter table public.meal_logs enable row level security;

create policy "users manage own profile" on public.profiles for all using (auth.uid() = id) with check (auth.uid() = id);
create policy "users manage own daily logs" on public.daily_logs for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
create policy "users manage own meals" on public.meal_logs for all using (auth.uid() = user_id) with check (auth.uid() = user_id);
