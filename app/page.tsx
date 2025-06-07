import { redirect } from "next/navigation"
import { cookies } from "next/headers"

export default function Home() {
  const cookieStore = cookies()
  const isAuthenticated = cookieStore.has("adminUser")

  if (isAuthenticated) {
    redirect("/dashboard")
  } else {
    redirect("/login")
  }
}
