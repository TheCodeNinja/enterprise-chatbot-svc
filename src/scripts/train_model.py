import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM, TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments

def main(model_name, output_dir, train_file):
    # Load pre-trained model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    # Prepare dataset
    dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=train_file,
        block_size=128
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Set up training arguments
    training_args = TrainingArguments(
        output_dir=output_dir,
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_steps=10_000,
        save_total_limit=2,
    )

    # Initialize Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=dataset,
    )

    # Train the model
    trainer.train()

    # Save the fine-tuned model
    trainer.save_model()
    tokenizer.save_pretrained(output_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fine-tune a language model for the chatbot")
    parser.add_argument("--model_name", default="gpt2", help="Pre-trained model name")
    parser.add_argument("--output_dir", required=True, help="Directory to save the fine-tuned model")
    parser.add_argument("--train_file", required=True, help="Path to the training data file")
    
    args = parser.parse_args()
    main(args.model_name, args.output_dir, args.train_file)