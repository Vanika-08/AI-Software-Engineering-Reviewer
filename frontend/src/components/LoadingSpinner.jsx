function LoadingSpinner() {
  return (
    <div className="text-center mt-5 mb-5">

      <div
        className="spinner-border text-primary"
        style={{
          width: "4rem",
          height: "4rem",
        }}
      />

      <h5 className="mt-3">
        AI is reviewing your project...
      </h5>

      <p className="text-muted">
        This may take a few seconds.
      </p>

    </div>
  );
}

export default LoadingSpinner;