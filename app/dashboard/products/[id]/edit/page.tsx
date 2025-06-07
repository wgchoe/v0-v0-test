import { ProductForm } from "@/components/product-form"
import { Button } from "@/components/ui/button"
import { ArrowLeft } from "lucide-react"
import Link from "next/link"
import { notFound } from "next/navigation"

// This would normally come from a database
const getProduct = (id: string) => {
  const products = [
    {
      id: "PROD-1",
      name: "Premium Laptop",
      description:
        "High-performance laptop with the latest processor, 16GB RAM, and 512GB SSD storage. Perfect for professionals and gamers alike.",
      category: "Electronics",
      price: 1299.99,
      stock: 45,
      sku: "LAP-PRO-2023",
    },
  ]

  return products.find((product) => product.id === id)
}

export default function EditProductPage({ params }: { params: { id: string } }) {
  const product = getProduct(params.id)

  if (!product) {
    notFound()
  }

  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center gap-2">
        <Button variant="outline" size="icon" asChild>
          <Link href={`/dashboard/products/${params.id}`}>
            <ArrowLeft className="h-4 w-4" />
          </Link>
        </Button>
        <h2 className="text-3xl font-bold tracking-tight">Edit Product</h2>
      </div>
      <div className="rounded-lg border p-6">
        <ProductForm
          initialData={{
            name: product.name,
            description: product.description,
            category: product.category,
            price: product.price,
            stock: product.stock,
            sku: product.sku,
          }}
          isEditing={true}
        />
      </div>
    </div>
  )
}
