import { Link, useLocation } from "wouter";
import { cn } from "@/lib/utils";
import { Wrench, BookOpen, AlertTriangle, Menu, X } from "lucide-react";
import { useState } from "react";

export default function Layout({ children }: { children: React.ReactNode }) {
  const [location] = useLocation();
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const navItems = [
    { href: "/", label: "Workshop", icon: Wrench },
    { href: "/mistakes", label: "Common Mistakes", icon: AlertTriangle },
  ];

  return (
    <div className="min-h-screen bg-[#1A1A1A] text-gray-100 font-sans selection:bg-[#FF6B00] selection:text-white">
      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-50 border-b border-[#4A5568] bg-[#1A1A1A]/95 backdrop-blur supports-[backdrop-filter]:bg-[#1A1A1A]/60">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="flex h-8 w-8 items-center justify-center rounded bg-[#FF6B00] text-black font-bold">
              <Wrench className="h-5 w-5" />
            </div>
            <span className="text-lg font-bold tracking-tight font-display uppercase">
              Oussama<span className="text-[#FF6B00]">.AutoTech</span>
            </span>
          </div>

          {/* Desktop Nav */}
          <nav className="hidden md:flex items-center gap-6">
            {navItems.map((item) => (
              <Link key={item.href} href={item.href}>
                <a
                  className={cn(
                    "flex items-center gap-2 text-sm font-medium transition-colors hover:text-[#FF6B00]",
                    location === item.href ? "text-[#FF6B00]" : "text-gray-400"
                  )}
                >
                  <item.icon className="h-4 w-4" />
                  {item.label}
                </a>
              </Link>
            ))}
          </nav>

          {/* Mobile Menu Button */}
          <button
            className="md:hidden p-2 text-gray-400 hover:text-white"
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X /> : <Menu />}
          </button>
        </div>
      </header>

      {/* Mobile Nav Menu */}
      {isMobileMenuOpen && (
        <div className="md:hidden border-b border-[#4A5568] bg-[#1A1A1A]">
          <nav className="container py-4 flex flex-col gap-4">
            {navItems.map((item) => (
              <Link key={item.href} href={item.href}>
                <a
                  className={cn(
                    "flex items-center gap-2 text-sm font-medium transition-colors hover:text-[#FF6B00]",
                    location === item.href ? "text-[#FF6B00]" : "text-gray-400"
                  )}
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  <item.icon className="h-4 w-4" />
                  {item.label}
                </a>
              </Link>
            ))}
          </nav>
        </div>
      )}

      <main className="container py-8">
        {children}
      </main>

      <footer className="border-t border-[#4A5568] bg-[#1A1A1A] py-8 mt-auto">
        <div className="container flex flex-col items-center justify-between gap-4 md:flex-row text-sm text-gray-500">
          <p>© 2025 Oussama's English Platform. Built for Mechanics.</p>
          <p className="flex items-center gap-1">
            <span className="h-2 w-2 rounded-full bg-[#00E676]"></span>
            System Operational
          </p>
        </div>
      </footer>
    </div>
  );
}
