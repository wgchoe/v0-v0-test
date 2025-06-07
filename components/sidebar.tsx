"use client"

import type React from "react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import { ScrollArea } from "@/components/ui/scroll-area"
import {
  BarChart3,
  Box,
  Building2,
  CircleUser,
  CreditCard,
  FileText,
  Home,
  Package,
  Settings,
  ShoppingCart,
  Users,
} from "lucide-react"
import Link from "next/link"
import { usePathname } from "next/navigation"

interface SidebarProps extends React.HTMLAttributes<HTMLDivElement> {}

export function Sidebar({ className }: SidebarProps) {
  const pathname = usePathname()

  const routes = [
    {
      label: "Dashboard",
      icon: Home,
      href: "/dashboard",
      variant: "default",
    },
    {
      label: "Analytics",
      icon: BarChart3,
      href: "/dashboard/analytics",
      variant: "ghost",
    },
    {
      label: "Customers",
      icon: Users,
      href: "/dashboard/customers",
      variant: "ghost",
    },
    {
      label: "Products",
      icon: Package,
      href: "/dashboard/products",
      variant: "ghost",
    },
    {
      label: "Orders",
      icon: ShoppingCart,
      href: "/dashboard/orders",
      variant: "ghost",
    },
    {
      label: "Invoices",
      icon: FileText,
      href: "/dashboard/invoices",
      variant: "ghost",
    },
    {
      label: "Payments",
      icon: CreditCard,
      href: "/dashboard/payments",
      variant: "ghost",
    },
    {
      label: "Suppliers",
      icon: Building2,
      href: "/dashboard/suppliers",
      variant: "ghost",
    },
    {
      label: "Inventory",
      icon: Box,
      href: "/dashboard/inventory",
      variant: "ghost",
    },
    {
      label: "Staff",
      icon: CircleUser,
      href: "/dashboard/staff",
      variant: "ghost",
    },
    {
      label: "Settings",
      icon: Settings,
      href: "/dashboard/settings",
      variant: "ghost",
    },
  ]

  return (
    <div className={cn("pb-12 border-r w-[250px] flex-shrink-0", className)}>
      <div className="space-y-4 py-4">
        <div className="px-4 py-2">
          <h2 className="mb-2 px-2 text-lg font-semibold tracking-tight">Main Menu</h2>
          <ScrollArea className="h-[calc(100vh-10rem)]">
            <div className="space-y-1">
              {routes.map((route) => (
                <Button
                  key={route.href}
                  variant={pathname === route.href ? "secondary" : "ghost"}
                  size="sm"
                  className="w-full justify-start"
                  asChild
                >
                  <Link href={route.href}>
                    <route.icon className="mr-2 h-4 w-4" />
                    {route.label}
                  </Link>
                </Button>
              ))}
            </div>
          </ScrollArea>
        </div>
      </div>
    </div>
  )
}
