function StructureCard({ structure }) {
  return (
    <div className="card shadow h-100 p-4">
      <h4>Project Structure</h4>

      {Object.entries(structure).map(([key, value]) => (
        <p key={key}>
          {value ? "✅" : "❌"} {key}
        </p>
      ))}
    </div>
  );
}

export default StructureCard;