import { ProductForm } from "@/components/product-form"

export default function NewProductPage() {
  return (
    <div className="flex flex-col gap-4">
      <div className="flex items-center justify-between">
        <h2 className="text-3xl font-bold tracking-tight">Add New Product</h2>
      </div>
      <div className="rounded-lg border p-6">
        <ProductForm />
      </div>
    </div>
  )
}
