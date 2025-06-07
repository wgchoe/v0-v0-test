// This would be replaced with actual API calls in a real application

export type User = {
  id: string
  name: string
  email: string
  role: "admin" | "user"
  avatar?: string
}

// Mock user database
const users = [
  {
    id: "1",
    name: "John Doe",
    email: "admin@example.com",
    password: "password", // In a real app, this would be hashed
    role: "admin" as const,
  },
  {
    id: "2",
    name: "Jane Smith",
    email: "user@example.com",
    password: "password", // In a real app, this would be hashed
    role: "user" as const,
  },
]

export async function authenticateUser(email: string, password: string): Promise<User | null> {
  // Simulate API delay
  await new Promise((resolve) => setTimeout(resolve, 500))

  const user = users.find((u) => u.email === email && u.password === password)

  if (!user) {
    return null
  }

  // Don't return the password
  const { password: _, ...userWithoutPassword } = user
  return userWithoutPassword
}

export async function getCurrentUser(userId: string): Promise<User | null> {
  // Simulate API delay
  await new Promise((resolve) => setTimeout(resolve, 300))

  const user = users.find((u) => u.id === userId)

  if (!user) {
    return null
  }

  // Don't return the password
  const { password: _, ...userWithoutPassword } = user
  return userWithoutPassword
}
