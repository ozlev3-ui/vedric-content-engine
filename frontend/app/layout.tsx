import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Vedric Content Engine",
  description: "Frontend skeleton for Vedric Content Engine"
};

export default function RootLayout({
  children
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-slate-950 text-slate-100">{children}</body>
    </html>
  );
}
